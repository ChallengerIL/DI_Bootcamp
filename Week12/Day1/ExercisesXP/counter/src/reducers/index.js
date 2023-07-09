import { createStore } from "redux";

const initialState = { count: 0 }

export const reducer = (state, action) => {
    let count = action.count;

    switch (action.type) {
      case "INCREASE_COUNT":
        count++;
        return {
            ...state,
            count: count,
        };
      case "DECREASE_COUNT":
        count--;
        return {
            ...state,
            count: count,
        };
      default:
        return state;
    };
  };

export const store = createStore(reducer, initialState);
  