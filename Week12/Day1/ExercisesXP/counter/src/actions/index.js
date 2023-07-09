const increase = count => {
    return {
        type: "INCREASE_COUNT",
        count: count
    }
}

const decrease = count => {
    return {
        type: "DECREASE_COUNT",
        count: count
    }
}

export {
    increase,
    decrease,
}