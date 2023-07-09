import { Component } from 'react';
import { connect } from 'react-redux';

class MovieDetails extends Component {
    render() {
        let title;
        let releaseDate;
        let rating;

        if (this.props.movie) {
            title = `Title: ${this.props.movie.title}`;
            releaseDate = `Release Date: ${this.props.movie.releaseDate}`;
            rating = `Rating: ${this.props.movie.rating}`;
          } else {
            title = "Select Movie";
            releaseDate = null;
            rating = null;
          }
        return (
            <>
                <h2>Movie</h2>
                <p>{ title }</p>  
                <p>{ releaseDate }</p>  
                <p>{ rating }</p>  
            </>
        )
    };
};

function MapStateToProps(state) {
    return {
        movie: state.movie,
    };
};

export default connect(MapStateToProps)(MovieDetails);
