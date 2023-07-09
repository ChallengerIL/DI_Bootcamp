import { Component } from 'react';
import { connect } from 'react-redux';
import { selectMovie } from '../actions';

class MovieList extends Component {
    handleClick = (movie) => {
        this.props.dispatch(selectMovie(movie));
    }

    render() {
        return(
            <div>
                <h2>MovieList</h2>
                { this.props.movies.map(movie =>
                    <div className='movieList' key={ movie.title }>
                        <span>{ movie.title }</span> 
                        <button onClick={() => this.handleClick(movie) }>details</button>
                    </div>
                ) }
            </div>
        )
    };
};

const MapStateToProps = state => {
    return {
        movies: state.movies,
    }
};

export default connect(MapStateToProps)(MovieList);
