import React, { Component } from 'react';
import { connect } from 'react-redux';
import Row from './Row';

 class TransactionForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            accountNumber: '',
            FSC: '',
            name: '',
            amount: '',
        }
    };

    handleInputChange = (e) => {

    }

    handleSubmit = (e) => {

    }

    render() {
        return (
            <div>
                <h1>Financial Transactions:</h1>
                <div className='container'>
                    <form onSubmit={this.handleSubmit}>
                        <input onChange={this.handleInputChange} type='text' name='accountNumber' placeholder='Account Number' />
                        <input onChange={this.handleInputChange} type='text' name='fsc' placeholder='FSC' />
                        <input onChange={this.handleInputChange} type='text' name='name' placeholder='A/C Holder Name' />
                        <input onChange={this.handleInputChange} type='text' name='amount' placeholder='Amount' />
                        <input type='submit' value='Submit' />
                    </form>
                    <hr />
                    <div id='transactions'>
                        {this.props.transactions.map(transaction => (
                            <Row transaction={transaction} key={transaction.id} />
                        ))}
                    </div>
                </div>
            </div>
        )
    }
}

const mapStateToProps = ({transactions}) => ({transactions});

export default connect(mapStateToProps)(TransactionForm);
