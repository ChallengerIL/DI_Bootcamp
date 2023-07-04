import { Component } from 'react';
import './App.css';

const url = "http://127.0.0.1:4000";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
        header: null,
        message: ''
    };
  };

  componentDidMount() {
    const makeRequest = async () => {
        const response = await fetch(`${url}/api/hello`, {method: 'GET'});
        const text = await response.text();
  
        this.setState({header: text});
    };
    
    makeRequest();
  };

  handleChange = (event) => {
    this.setState(
      { [event.target.name]: event.target.value }
      );
	};

  makePostRequest = async (event) => {
    event.preventDefault();

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({message : this.state.message})
    }; 

    const response = await fetch(`${url}/api/world`, requestOptions);
    const text = await response.text();

    this.setState({response: text});
  };

  render() {
    const header = this.state.header;
    const response = this.state.response;
    return (
      <main>
        <h1>{header}</h1>
        <h2>Post to Server:</h2>
        <form onSubmit={this.makePostRequest}>
          <input type="text" onChange={this.handleChange} name='message' />
          <button type="submit">Submit</button>
        </form>
        {response}
      </main>
    );
  };
};

export default App;
