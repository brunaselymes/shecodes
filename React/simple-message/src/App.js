import React from "react";

function App() {
  const [message, setMessage] = React.useState("JavaScriptis socool.");

  function handleClick() {
    setMessage("my new message");
  }

  return (
    <div>
      <h1>{message}</h1>
      <button onClick={handleClick}>Update the message!</button>
    </div>
  );
}

export default App;
