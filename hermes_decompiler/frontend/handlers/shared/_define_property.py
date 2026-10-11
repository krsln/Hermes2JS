from __future__ import annotations

from hermes_decompiler.ir.expressions import (
    BooleanLiteral, CallExpression, Expression, Identifier, MemberExpression, ObjectExpression, ObjectProperty,
)


def define_non_enumerable(obj: Expression, key: Expression, value: Expression) -> CallExpression:
    """`Object.defineProperty(obj, key, { value, writable, enumerable: false, configurable })`.

    What `DefineOwnByVal`/`PutOwnByVal` with the enumerable flag clear do (a
    class method, say). A plain `obj[key] = value` would make the property
    enumerable and run a setter on the way, so it says something else.
    """

    def entry(name: str, expression: Expression) -> ObjectProperty:
        return ObjectProperty(key=Identifier(name=name), value=expression, shorthand=False, computed=False)

    descriptor = ObjectExpression(
        properties=(
            entry("value", value),
            entry("writable", BooleanLiteral(value=True)),
            entry("enumerable", BooleanLiteral(value=False)),
            entry("configurable", BooleanLiteral(value=True)),
        )
    )

    return CallExpression(
        callee=MemberExpression(obj=Identifier(name="Object"), prop=Identifier(name="defineProperty"), computed=False),
        arguments=(obj, key, descriptor),
    )
