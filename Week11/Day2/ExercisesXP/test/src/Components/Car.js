import { Component } from 'react';
import Garage from './Garage';

class Car extends Component {
    constructor(props) {
      super(props);
      this.state = {
        color: "black"
      };
    }
  
    render() {
      return (
        <div>
            <h1>This car is a { this.state.color } { this.props.model }</h1>
            <Garage size="small" />
        </div> 
      )
    }
}
  
export default Car;