import { Component } from 'react';

class Color extends Component {
    constructor() {
        super();
        this.state = {
            favoriteColor: "red"
        };
      }

    changeColor = () => {
        this.setState(
            {
              favoriteColor: "blue"
            }
        )
    }

    componentDidMount() {
        setTimeout(() => {
            this.setState(
                {
                  favoriteColor: "yellow"
                }
            );
          }, 5000);
    }

    render() {
      return (
        <div>
            <h1>My favorite color is <i>{ this.state.favoriteColor }</i></h1>
            <button onClick={ this.changeColor }>Change color</button>
        </div>
      )
    }
}
  
export default Color;