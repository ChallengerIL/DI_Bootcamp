import './App.css';
import { Component } from 'react';

class App extends Component {
  constructor() {
    super()
    this.state = {
      languages : [
          {name: "Php", votes: 0},
          {name: "Python", votes: 0},
          {name: "JavaSript", votes: 0},
          {name: "Java", votes: 0}
      ]
    }
  }

  increaseVoteCount = (e) => {
    let languages = [...this.state.languages];
    let language = {...languages[e.target.value]};
    language.votes++;
    languages[e.target.value] = language;
    
    this.setState({languages});
  }

  render() {

    return (
      <div className='App'>
        <h1>Vote Your Language!</h1>
        <div className='languages'>
            {
              this.state.languages.map((language, index) => (
                <div key={index} className='language'>
                  <div className='votes'>{language.votes}</div>
                  <div className='name'>{language.name}</div>
                  <button value={index} onClick={this.increaseVoteCount}>Click Here</button>
                </div>
              ))
            }
        </div>
      </div>
    )
  }
}

export default App;
