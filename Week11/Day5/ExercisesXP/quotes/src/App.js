import './App.css';
import { Component } from 'react';
import quotes from './QuotesDatabase';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      quote: "",
      author: "",
      color: "",
      index: quotes.length + 1,
      slide: false
    }
  }

  componentDidMount() {
    this.handleClick();
  }

  handleClick = () => {
    let randomNumber;

    do {
      randomNumber = Math.floor(Math.random() * quotes.length);
    } while (randomNumber === this.state.index);
    
    let item = quotes[randomNumber];
    let newColor = `#${Math.floor(Math.random()*16777215).toString(16)}`;

    this.setState({
      quote: item.quote,
      author: item.author,
      color: newColor,
      index: randomNumber,
      slide: true
    });
  };

  render() {
    const author = this.state.author.length > 0 ? this.state.author : "Unknown";
    const slide = this.state.slide;

    return (
      <main style={{backgroundColor: `${this.state.color}`}}>
        <div id="card">
          <div className={slide ? 'slide' : ''} onAnimationEnd={() => this.setState({ slide: false })} id="slider">
            <div className="row quote">
              <h1 style={{color: `${this.state.color}`}}>"{this.state.quote}"</h1>
            </div>
            <div className="row author">
              <p style={{color: `${this.state.color}`}}><i>-{author}-</i></p>
            </div>
          </div>
          <div className="row button">
            <button onClick={this.handleClick} style={{backgroundColor: `${this.state.color}`}}>New quote</button>
          </div>
        </div>
      </main>
    );
  };
};
