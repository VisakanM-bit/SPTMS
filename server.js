const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Your MongoDB Atlas credentials
const username = "visakan2005smr"; // Your MongoDB username (NOT email)
const password = encodeURIComponent("visakan@2005"); // Encoded to handle special characters
const dbName = "mydb";

// MongoDB Atlas connection URI
const uri = `mongodb+srv://${username}:${password}@cluster0.npryo.mongodb.net/${dbName}?retryWrites=true&w=majority`;

// Connect to MongoDB
mongoose.connect(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log("✅ MongoDB connected successfully!"))
.catch(err => console.error("❌ MongoDB connection error:", err));

// Simple test route
app.get("/", (req, res) => {
    res.send("🚀 Server is running and connected to MongoDB!");
});

// Start server
app.listen(3000, () => {
    console.log("🌍 Server started on http://localhost:3000");
});
