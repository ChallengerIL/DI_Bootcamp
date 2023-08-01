import React, { Component } from 'react'

export default class Row extends Component {
    constructor(props) {
        super(props);
    };

    render() {
        return (
        <>
            <span>{this.props.transaction.accountNumber}</span>
            <span>{this.props.transaction.fsc}</span>
            <span>{this.props.transaction.name}</span>
            <span>{this.props.transaction.amount}</span>
        </>
        )
    }
}
