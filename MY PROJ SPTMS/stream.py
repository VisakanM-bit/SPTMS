import streamlit as st

# Make Streamlit use the full width of the page
st.set_page_config(layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Home - SPTMS</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
  body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: url("https://raw.githubusercontent.com/VisakanM-bit/SPTMS/refs/heads/main/MY%20PROJ%20SPTMS/image.png") no-repeat center center fixed;
    background-size: cover;
    color: rgb(243, 237, 237);
  }
  .heading-box {
    border: 2px solid #0f0101;
    padding: 20px;
    text-align: center;
    display: inline-block;
    margin: 20px auto;
    border-radius: 8px;
    background-color: #03000a;
    box-shadow: 0 0 10px rgba(243, 242, 242, 0.1);
  }
  .scroll-message {
    background-color: #333;
    color: white;
    padding: 5px;
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px; 
  }
  .split-section {
    display: flex;
    max-width: 1200px; 
    margin: auto;
    padding: 20px;
    gap: 20px;
  }
  .left-side {
    flex: 2;
  }
  .right-side {
    flex: 1;
  }
  .left-side, .right-side {
    background-color: rgba(243, 236, 236, 0.1);
    border-radius: 8px;
    padding: 20px;
  }
  .left-side h2 {
    color: #ece3e3;
  }
  ul {
    padding-left: 20px;
  }
  .login-container form {
    display: flex;
    flex-direction: column;
    gap: 12px;
    background-color: rgba(0,0,0,0.3);
    padding: 20px;
    border-radius: 8px;
    width: 100%;
  }
  .login-container input, 
  .login-container button {
    padding: 10px;
    border: none;
    border-radius: 4px;
    outline: none;
  }
  .login-container button {
    background-color: #ff9800;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s;
  }
  .login-container button:hover {
    background-color: #e68900;
  }
  .logo {
    max-width: 200px;
    height: auto;
    position: absolute;
    top: 20px;
  }
  .logo.left {
    left: 40px;
  }
  .logo.right {
    right: 40px;
  }
  @media (max-width: 768px) {
    .split-section {
      flex-direction: column;
    }
    .logo {
      position: static;
      display: block;
      margin: auto;
    }
  }
  </style>
</head>
<body>
  <img src="https://raw.githubusercontent.com/VisakanM-bit/SPTMS/refs/heads/main/MY%20PROJ%20SPTMS/buslogo1.jpg" alt="Bus Logo" class="logo left">
  <img src="https://raw.githubusercontent.com/VisakanM-bit/SPTMS/refs/heads/main/MY%20PROJ%20SPTMS/clglogo1.jpg" alt="College Logo" class="logo right">

  <div style="text-align:center;">
    <div class="heading-box">
      <h1>Smart Public Transport Management System</h1>
    </div>
  </div>

  <marquee class="scroll-message" behavior="scroll" direction="left">
    Welcome to Smart Public Transport Management System – Efficient, Reliable & Smart Public Transport Solutions!
  </marquee>

  <div class="split-section">
    <div class="left-side">
      <p style="font-weight: bold; font-size: 40px; line-height: 1.4;">
        FROM STOP TO DESTINATION<br> WE HAVE GOT YOU COVERED
      </p>
      <p style="font-weight: bold; font-size: 16px; line-height: 1.4; margin-top: 0;">
        AI-powered system for real-time bus tracking, crowd prediction, and safety monitoring.
        Ensuring smoother, safer, and smarter journeys for everyone.
      </p>
      <h2>Contact Details</h2>
      <p>Email: visakan2005smr@gmail.com</p>
      <p>Phone: 9514221814</p>
    </div>
    <div class="right-side">
      <h2>Login</h2>
      <div class="login-container">
        <form>
          <input type="text" placeholder="Username" required>
          <input type="text" placeholder="Phone number" required>
          <button type="button">Get the code</button>
          <input type="text" placeholder="Enter the code" required>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  </div>
</body>
</html>
"""

st.components.v1.html(html_code, height=1200, scrolling=True)
