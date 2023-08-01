import { combineReducers } from "redux";

const initialState = [{id: 1, accountNumber: 'accounwft number', fsc: 'fsc', name: 'name', amount: 'amount'}, {id: 2, accountNumber: 'account number', fsc: 'fsc', name: 'name', amount: 'amount'}, {id: 3, accountNumber: 'account number', fsc: 'fsc', name: 'name', amount: 'amount'}];

function transactionReducer(state = initialState, action) {
    return state;
}

// function reducer(state, action) {
    // switch (action.type) {
    //     case INSERT:
    //         return action.movie;
    //     default:
    //         return state;
    // }
// }

export const rootReducer = combineReducers({
    transactions: transactionReducer,
})
