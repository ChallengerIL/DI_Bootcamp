import { Component } from 'react';

class Child extends Component {
    componentWillUnmount() {
        alert("The component named Header is about to be unmounted.");
    }

    render() {
        return (
            <h1>Hello World!</h1>
        )
    }
}

class Color extends Component {
    constructor(props) {
        super(props);
        this.state = {
            favoriteColor: "red",
            show: true
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

    // shouldComponentUpdate() {
    //     return false;
    // }

    getSnapshotBeforeUpdate() {
        console.log("in getSnapshotBeforeUpdate");
    }

    componentDidUpdate() {
        console.log("after update");
    }

    deleteHeader = () => {
        this.setState(
            {
                show: false
            }
        )
    }

    render() {
        let comp;
        if (this.state.show) {
            comp = <Child />;
          }

      return (
        <div>
            {
            comp ? 
            comp :
            <h1>My favorite color is <i>{ this.state.favoriteColor }</i></h1>
        }

            <button onClick={ this.deleteHeader }>Delete Header</button>
            
            <button onClick={ this.changeColor }>Change color</button>
        </div>
      )
    }
}
  
export default Color;