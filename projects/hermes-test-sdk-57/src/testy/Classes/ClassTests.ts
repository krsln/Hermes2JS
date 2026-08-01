class Animal {
    protected name: string;
    private sound: string;

    constructor(name: string, sound: string) {
        console.log("__BC:Classes/ClassTests/Animal/constructor");
        this.name = name;
        this.sound = sound;
    }

    makeSound(): void {
        console.log("__BC:Classes/ClassTests/Animal/makeSound");
        console.log(this.name, "says", this.sound);
    }

    get description(): string {
        console.log("__BC:Classes/ClassTests/Animal/get-description");
        return `${this.name} the animal`;
    }
}

class Dog extends Animal {
    private breed: string;

    constructor(name: string, breed: string) {
        super(name, "Woof");
        console.log("__BC:Classes/ClassTests/Dog/constructor");
        this.breed = breed;
    }

    override makeSound(): void {
        console.log("__BC:Classes/ClassTests/Dog/makeSound-override");
        super.makeSound();
        console.log(this.name, "is a", this.breed);
    }

    static create(name: string): Dog {
        console.log("__BC:Classes/ClassTests/Dog/static-create");
        return new Dog(name, "Mixed");
    }
}

export function classTest() {
    console.log("__BC:Classes/ClassTests/classTest/start");

    const animal = new Animal("Generic", "...");
    animal.makeSound();
    console.log(animal.description);

    const dog = new Dog("Rex", "Labrador");
    dog.makeSound();

    const asAnimal: Animal = dog;
    asAnimal.makeSound();

    const created = Dog.create("Buddy");
    created.makeSound();

    console.log("__BC:Classes/ClassTests/classTest/end");
}
