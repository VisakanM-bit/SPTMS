import streamlit as st

# Force Streamlit page to go full width
st.set_page_config(layout="wide")

# Remove default Streamlit padding and center lock
st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Home - SPTMS</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    html, body {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      font-family: Arial, sans-serif;
      background: url("https://raw.githubusercontent.com/VisakanM-bit/SPTMS/refs/heads/main/MY%20PROJ%20SPTMS/image.png") no-repeat center center fixed;
      background-size: cover;
      color: rgb(243, 237, 237);
    }
    .heading-box {
      border: 2px solid #0f0101;
      padding: 20px;
      text-align: center;
      border-radius: 8px;
      background-color: #03000a;
      display: inline-block;
      margin: 160px auto 20px;
      box-shadow: 0 0 10px rgba(243, 242, 242, 0.1);
    }
    .scroll-message {
      background-color: #333;
      color: white;
      padding: 8px;
      font-size: 1.2rem;
      font-weight: bold;
      width: 100%;
    }
    .split-section {
      display: flex;
      flex-wrap: wrap;
      width: 100%;
      padding: 20px;
      gap: 20px;
      box-sizing: border-box;
    }
    .left-side, .right-side {
      flex: 1 1 300px;
      background-color: rgba(243, 236, 236, 0.1);
      border-radius: 8px;
      padding: 20px;
    }
    .login-container form {
      display: flex;
      flex-direction: column;
      gap: 12px;
      background-color: rgba(0,0,0,0.3);
      padding: 20px;
      border-radius: 8px;
      max-width: 350px;
      margin: auto;
    }
    .login-container input, 
    .login-container button {
      padding: 10px;
      border: none;
      border-radius: 4px;
    }
    .login-container button {
      background-color: #ff9800;
      color: white;
      cursor: pointer;
    }
    .login-container button:hover {
      background-color: #e68900;
    }
    img.logo {
      max-width: 250px;
      width: 20vw;
      position: absolute;
      top: 20px;
    }
    .logo.left { left: 40px; }
    .logo.right { right: 40px; }
    @media (max-width: 768px) {
      img.logo {
        max-width: 150px;
      }
    }
  </style>
</head>
<body>
  <img src="https://raw.githubusercontent.com/VisakanM-bit/SPTMS/refs/heads/main/MY%20PROJ%20SPTMS/buslogo1.jpg" class="logo left">
  <img src="https://raw.githubusercontent.com/VisakanM-bit/SPTMS/refs/heads/main/MY%20PROJ%20SPTMS/clglogo1.jpg" class="logo right">

  <div style="text-align:center;">
    <div class="heading-box">
      <h1>Smart Public Transport Management System</h1>
    </div>
  </div>

  <marquee class="scroll-message">
    Welcome to Smart Public Transport Management System – Efficient, Reliable & Smart Public Transport Solutions!
  </marquee>

  <div class="split-section">
    <div class="left-side">
      <p style="font-weight:bold;font-size:2rem;line-height:1.4;">
        FROM STOP TO DESTINATION<br> WE HAVE GOT YOU COVERED
      </p>
      <p style="font-weight:bold;font-size:1rem;line-height:1.4;">
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

st.components.v1.html(html_code, height=1000, scrolling=True)
