// True private fields (#name), static fields/methods/blocks, and
// getter+setter pairs on the same property - all distinct bytecode
// shapes from ClassTests.ts's public-field inheritance case.

class Counter {
    #count: number = 0;
    static #instances: number = 0;

    static readonly MAX = 100;

    constructor() {
        console.log("__BC:Classes/PrivateStaticTests/Counter/constructor");
        Counter.#instances++;
    }

    get value(): number {
        console.log("__BC:Classes/PrivateStaticTests/Counter/get-value");
        return this.#count;
    }

    set value(v: number) {
        console.log("__BC:Classes/PrivateStaticTests/Counter/set-value");
        this.#count = Math.min(v, Counter.MAX);
    }

    increment(): number {
        console.log("__BC:Classes/PrivateStaticTests/Counter/increment");
        return ++this.#count;
    }

    #privateHelper(): string {
        return `count=${this.#count}`;
    }

    describe(): string {
        console.log("__BC:Classes/PrivateStaticTests/Counter/describe");
        return this.#privateHelper();
    }

    static get instanceCount(): number {
        console.log("__BC:Classes/PrivateStaticTests/Counter/static-get-instanceCount");
        return Counter.#instances;
    }

    static reset(): void {
        console.log("__BC:Classes/PrivateStaticTests/Counter/static-reset");
        Counter.#instances = 0;
    }
}

class ConfiguredCounter extends Counter {
    static #label = "configured";

    static {
        console.log("__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block");
        ConfiguredCounter.#label = ConfiguredCounter.#label.toUpperCase();
    }

    static describeLabel(): string {
        return ConfiguredCounter.#label;
    }
}

export function privateStaticTest() {
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/start");

    const c1 = new Counter();
    const c2 = new Counter();

    c1.increment();
    c1.increment();
    c1.value = 200; // clamped by the setter

    console.log(c1.value);
    console.log(c1.describe());
    console.log(Counter.instanceCount);

    console.log(ConfiguredCounter.describeLabel());

    Counter.reset();
    console.log(Counter.instanceCount);

    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/end");
}
