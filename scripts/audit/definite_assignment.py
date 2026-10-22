"""Rough definite-assignment check on decompiled output.

Reports registers read where they are not definitely assigned on every path
(structured if/else only; for-of / for-in heads and switch arms give false
positives, so compare two runs instead of trusting absolute numbers).

usage: python3 scripts/audit/definite_assignment.py <file.js | directory> [...]
"""
import re,sys
REG=re.compile(r'\br(\d+)\b')
ASSIGN=re.compile(r'^(r\d+)\s*=[^=>]')
def check(text):
    lines=[l.strip() for l in text.split('\n') if l.strip() and not l.strip().startswith('//')]
    # stack frames: (kind, assigned_in_branch_sets)
    cur=set(); stack=[]; bad=[]
    # frame: dict(kind, base(set at entry), branches(list of sets finished), terminated flag per branch)
    term=False
    def reads(expr):
        return {f"r{m}" for m in REG.findall(expr)}
    for ln in lines:
        if re.match(r'^(async )?function',ln): continue
        if ln.startswith('}') :
            # closing; maybe "} else {" / "} else if (...) {" / "} while (...);"
            if not stack: continue
            fr=stack[-1]
            fr['branches'].append((cur,term))
            if re.match(r'^\}\s*else',ln):
                cur=set(fr['base']); term=False
                # reads in else-if condition
                m=re.match(r'^\}\s*else if \((.*)\)\s*\{',ln)
                if m:
                    for r in reads(m.group(1))-cur: bad.append((r,ln))
                fr['has_else']=True if not m else fr.get('has_else',False)
                if m: fr['has_else']=False
                continue
            stack.pop()
            live=[b for b,t in fr['branches'] if not t]
            if fr['kind']=='if':
                if fr.get('has_else'):
                    cur=set.intersection(*live) if live else set(fr['base'])
                    term=(not live)
                else:
                    cur=set(fr['base']) if not fr['branches'][0][1] or True else cur
                    # no else: assigned-after = base (conservative)
                    term=False
            else:
                cur=set(fr['base'])|(set.intersection(*live) if live and fr['kind']=='do' else set())
                term=False
            m=re.match(r'^\}\s*while \((.*)\);',ln)
            if m:
                for r in reads(m.group(1))-cur: bad.append((r,ln))
            continue
        m=re.match(r'^(if|while|for|switch|do)\b(.*)\{$',ln)
        if m or ln=='do {':
            kind=m.group(1) if m else 'do'
            expr=m.group(2) if m else ''
            for r in reads(expr)-cur-{f"r{x}" for x in []}: bad.append((r,ln))
            stack.append({'kind':'if' if kind=='if' else kind,'base':set(cur),'branches':[],'has_else':False})
            if kind=='if': pass
            continue
        if re.match(r'^(case .*|default):$',ln): cur=set(stack[-1]['base']) if stack else cur; continue
        if term: continue
        mm=ASSIGN.match(ln)
        rhs=ln.split('=',1)[1] if mm else ln
        for r in reads(rhs)-cur: bad.append((r,ln))
        if mm: cur.add(mm.group(1))
        if ln.startswith(('return','throw')): term=True
    return bad
def main(argv=None):
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Rough definite-assignment check on decompiled .js output "
                    "(prints register reads that are not assigned on every path).")
    parser.add_argument("paths", nargs="+", help="decompiled .js files, or directories of them")
    args = parser.parse_args(argv)

    total = 0
    for given in args.paths:
        path = Path(given)
        files = sorted(path.glob("*.js")) if path.is_dir() else [path]
        for file in files:
            bad = check(file.read_text(encoding="utf-8"))
            total += len(bad)
            for register, line in bad:
                print(f"{file.name}: {register}  {line}" if len(files) > 1 else f"{register}  {line}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
