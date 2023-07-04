import './App.css';
import { Component } from 'react';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: 1,
      todo: '',
      todos: []
    }
  }

  handleDelete = (toDelete) => {
    const arr = this.state.todos.filter((item) => item !== toDelete);
    this.setState({todos: arr});
  }

  handleChange = (event) => {
    this.setState(
      { [event.target.name]: event.target.value }
    )
	}

  handleSubmit = (event) => {
    event.preventDefault();
    let todos = [...this.state.todos];
    const newTodo = {
      id: this.state.id,
      todo: event.target.todo.value
    }

    todos.push(newTodo);
    this.setState({
      id: this.state.id + 1,
      todo: '',
      todos: todos
    });
  };

  render() {
    
    return (
      <div className='container'>
        <h1>Todo's</h1>
        <div className='todos'>
        {this.state.todos.map(todo => <div key={todo.id} className='todo'>
          <span onClick={() => this.handleDelete(todo)}>{todo.todo}</span>
          </div>)}
        </div>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="todo">Add a new todo:</label><br />
          <input type="text" onChange={this.handleChange} value={this.state.todo} id="todo" name="todo" />
        </form>
      </div>
    );
  };
};
