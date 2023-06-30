import { Component } from 'react';

class Garage extends Component {
  
    render() {
      return (
        <p>Who lives in my { this.props.size } Garage?</p>
      )
    }
}
  
export default Garage;