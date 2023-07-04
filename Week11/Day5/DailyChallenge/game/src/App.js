import './App.css';
import { Component } from 'react';
import superheroes from './superheroes.json';

export default class App extends Component {
  state = {
    score: 0,
    topScore: 0,
    superheroes: superheroes.superheroes
  };

  shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    };
    return arr;
  };

  handleClick = (hero) => {
    let choice = this.state.superheroes.filter(person => person.id === hero.id)[0];
    
    if (!choice.clicked) {
      
      const updatedArr = this.state.superheroes.map(obj => {
        if (obj.id === hero.id) {
          return {...obj, clicked: true};
        }
        return obj;
      });

      this.setState(prevState => ({
        score: prevState.score + 1
      }));

      this.setState({superheroes: updatedArr});

    } else {

      if (this.state.score > this.state.topScore) {
        this.setState({
          topScore: this.state.score
        });
      };

      this.setState({
        score: 0,
        superheroes: superheroes.superheroes
      });
    };
  };

  render() {
    const heroes = this.shuffle([...this.state.superheroes]);

    return (
      <div className="App">
        <nav>
          <div className="top-header">
            <h1>Superheroes Memory Game</h1>
            <div>
              <p>Score: <span>{this.state.score}</span></p>
              <p>Top Score: <span>{this.state.topScore}</span></p>
            </div>
          </div>
          <div className="info">
            <h2>Get points by clicking on an image but don't click on any more than once!</h2>
          </div>
        </nav>
        <div className='container'>
          {heroes.map(hero => 
          <div key={hero.id} className='card' onClick={() => this.handleClick(hero)}>
            <img src={hero.image} alt={hero.name} />
            <p><strong>Name:</strong> {hero.name}</p>
            <p><strong>Occupation:</strong> {hero.occupation}</p>
          </div>
          )}
        </div>
      </div>
    );
  };
};
