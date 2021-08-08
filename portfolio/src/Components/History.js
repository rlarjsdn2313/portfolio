import React from 'react';
import PropTypes from 'prop-types';


function Movie({ title, description, date }) {
      return (
            <div className="History">
                  <div className="title">
                        - {title}
                  </div>
                  <div className="description">
                        - {description}
                  </div>
                  <div className="date">
                        - {date}
                  </div>
            </div>
      );
}


Movie.propTypes = {
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      date: PropTypes.array.isRequired
};

export default Movie;
