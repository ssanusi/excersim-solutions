class HelloWorld {
    static hello(arg?:string) : string {
        // Your code here
        if(arg) return `Hello, ${arg}!`
        return 'Hello, World!'
    }
}

export default HelloWorld