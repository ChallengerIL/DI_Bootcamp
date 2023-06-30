import { Component } from 'react';

class Events extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isToggleOn: true
        };
      }

    clickMe = () => {
        alert("I was clicked");
    }

    switcher = () => {
        let val;

        if (this.state.isToggleOn) {
            val = false;
        } else {
            val = true;
        }

        this.setState({
            isToggleOn: val
        });
    }

    handleKeyDown = (e) => {
    if (e.key === 'Enter') {
        alert(`The Enter key was pressed, your input is: ${e.target.value}`);
    }
    }

    render() {
      return (
        <div>
            <button
            type="button"
            onClick={ this.clickMe }
            >Click Me</button><br /><br />
            <input onKeyDown={ this.handleKeyDown } placeholder='Press the ENTER key!' /><br /><br />
            <button
            type="button"
            onClick={ this.switcher }
            >
                {this.state.isToggleOn ? "ON" : "OFF"}
            </button>
        </div>
      )
    }
}
  
export default Events;