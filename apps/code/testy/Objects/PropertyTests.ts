export function propertyAccessTest() {
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/start");

    const obj: { [key: string]: number } = {
        x: 1,
        y: 2
    };

    obj["z"] = 3;

    console.log(obj.x, obj["y"], obj.z);

    delete obj.x;

    console.log("x" in obj);

    for (const key of Object.keys(obj)) {
        console.log(key, obj[key]);
    }

    console.log("__BC:Objects/PropertyTests/propertyAccessTest/end");
}

export function computedPropertyTest() {
    console.log("__BC:Objects/PropertyTests/computedPropertyTest/start");

    const key = "dynamic";

    const obj = {
        [key]: 42,
        ["static" + "Key"]: "value"
    };

    console.log(obj);

    console.log("__BC:Objects/PropertyTests/computedPropertyTest/end");
}

export function optionalChainingTest() {
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/start");

    const data: { a?: { b?: { c?: number } } } = { a: { b: {} } };

    const value = data?.a?.b?.c ?? -1;

    console.log(value);

    console.log("__BC:Objects/PropertyTests/optionalChainingTest/end");
}
