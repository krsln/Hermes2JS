// Map/Set/WeakMap - built-in iterables whose iteration goes through
// Symbol.iterator, a different path than plain array/object iteration
// already covered in IteratorTests/ForEachTests.

export function mapTest() {
    console.log("__BC:Collections/MapSetTests/mapTest/start");

    const scores = new Map<string, number>();
    scores.set("alice", 90);
    scores.set("bob", 75);
    scores.set("carol", 88);

    console.log(scores.get("bob"));
    console.log(scores.has("dave"));
    console.log(scores.size);

    for (const [name, score] of scores) {
        console.log(name, score);
    }

    scores.delete("bob");
    console.log(scores.size);

    console.log("__BC:Collections/MapSetTests/mapTest/end");
}

export function setTest() {
    console.log("__BC:Collections/MapSetTests/setTest/start");

    const unique = new Set([1, 2, 2, 3, 3, 3]);
    console.log(unique.size);

    unique.add(4);
    console.log(unique.has(2));

    for (const value of unique) {
        console.log(value);
    }

    const asArray = [...unique];
    console.log(asArray);

    console.log("__BC:Collections/MapSetTests/setTest/end");
}

export function weakMapTest() {
    console.log("__BC:Collections/MapSetTests/weakMapTest/start");

    const wm = new WeakMap<object, string>();
    const key = {};
    wm.set(key, "value");

    console.log(wm.has(key));
    console.log(wm.get(key));

    console.log("__BC:Collections/MapSetTests/weakMapTest/end");
}

export function callMapSetTests() {
    console.log("__BC:Collections/MapSetTests/callMapSetTests/start");

    mapTest();
    setTest();
    weakMapTest();

    console.log("__BC:Collections/MapSetTests/callMapSetTests/end");
}
