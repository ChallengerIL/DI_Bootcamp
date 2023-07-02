import './App.css';
import { Component } from 'react';

class FormComponent extends Component {
  state = {};

  handleChange = (event) => {
    this.setState(
      event.target.type !== 'checkbox' ?
      { [event.target.name]: event.target.value } :
      { [event.target.name]: event.target.checked }
      )
	}

  render() {
    return (
      <>
        <form method='GET'>
          <input type="text" value={this.state.firstName} name='firstName' placeholder='First Name' onChange={this.handleChange} /><br /><br />
          <input name="lastName" type="text" placeholder='Last Name' onChange={this.handleChange} /><br /><br />
          <input name="age" type="number" placeholder='Age' onChange={this.handleChange} /><br /><br />
          <input type="radio" name="gender"
              value="male" onChange={this.handleChange} />
          Male<br />
          <input type="radio" name="gender"
              value="female" onChange={this.handleChange} />
          Female<br />
          <label>Select your destination</label><br />
          <select name="destination" onChange={this.handleChange}>
              <option value="" disabled selected>
                  -- Please Choose a destination --
              </option>
                  <option value="Thailand">Thailand</option>
                  <option value="Japan">Japan</option>
                  <option value="Brazil">Brazil</option>
          </select><br /><br />
          <label htmlFor="diet">Dietary restrictions:</label><br />
          <input type="checkbox" name="nutsFree" onChange={this.handleChange} />
          Nuts free<br />
          <input type="checkbox" name="lactoseFree" onChange={this.handleChange} />
          Lactose free<br />
          <input type="checkbox" name="vegan" onChange={this.handleChange} />
          Vegan
          <br /><br />
          <button type="submit">Submit</button>
        </form>
        <hr />
        <div>
          <h2>Entered information:</h2>
          <p>Your name: {this.state.firstName} {this.state.lastName}</p>
          <p>Your age: {this.state.age}</p>
          <p>Your gender: {this.state.gender}</p>
          <p>Your destination: {this.state.destination}</p>
          <p>Your dietary restrictions:</p>
          <p>**Nuts free : {this.state.nutsFree ? 'Yes' : 'No'}</p>
          <p>**Lactose free : {this.state.lactoseFree ? 'Yes' : 'No'}</p>
          <p>**Vegan meal : {this.state.vegan ? 'Yes' : 'No'}</p>
          {this.state.nutsFree}
        </div>
      </>
    )
  }
}

class App extends Component {
	render() {
		return (
      <main>
        <FormComponent />
      </main>
		);
	}
}

export default App;
