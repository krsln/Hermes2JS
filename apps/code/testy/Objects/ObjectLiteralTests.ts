export function objectLiteralTest() {
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start");

    const person = {
        name: "Ada",
        age: 30,
        greet() {
            console.log("hello", this.name);
        }
    };

    console.log(person.name, person.age);
    person.greet();

    const { name, age } = person;
    console.log(name, age);

    const nested = {
        a: 1,
        b: {
            c: 2,
            d: {
                e: 3
            }
        }
    };

    console.log(nested.b.d.e);

    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end");
}
