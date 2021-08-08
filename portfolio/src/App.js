import React from 'react'
import axios from 'axios'

import History from './Components/History';


class App extends React.Component {
  state = {
    isLoading: true,
    history: []
  };

  getHistory = async () => {
    const {
      data: {
        history
      }
    } = await axios.get('http://localhost:5000/history');

    this.setState({ history, isLoading: false});
  };

  componentDidMount() {
    this.getHistory()
  }


  render() {
    const { isLoading, history } = this.state;
    return (
      <div>
        { isLoading ? "Loading..." : 
        history.map(history => (
          <History
            key={ history.id }
            title={ history.title }
            description={ history.description }
            date={ history.date } 
          />
        ))}
      </div> 
    );
  };
}

export default App;
