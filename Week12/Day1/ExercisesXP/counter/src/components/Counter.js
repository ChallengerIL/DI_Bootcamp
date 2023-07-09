import React from "react";
import { store } from '../reducers';
import { increase, decrease } from "../actions";

const Counter = ({ count=store.getState().count }) => {

    const handleSubmit = event => {
        event.preventDefault();
        const buttonType = event.target.dataset.button
        const counter = event.target.parentElement.firstElementChild.dataset.counter

        switch (buttonType) {
            case "increase":
                store.dispatch(increase(counter));
                break;
            case "decrease":
                store.dispatch(decrease(counter));
                break;
            default:
                console.log("wrong button")
        }
    }


    return (
        <>
            <h1 data-counter={count}><span>{count}</span></h1>
            <button type="submit" onClick={handleSubmit} data-button="increase">+</button>
            <button type="submit" onClick={handleSubmit} data-button="decrease">-</button>
        </>
    );
};

export default Counter;
