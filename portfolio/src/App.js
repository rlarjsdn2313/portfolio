import React from 'react'
import axios from 'axios'

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
    return (
      <div>
        hello!
      </div>
    );
  };
}

export default App;
