const express = require("express");
const mongoose = require("mongoose");
const schema = require("./model").question;
const app = express();

PASSWORD = "ss123546";
PORT = 8000;
URL = `mongodb+srv://kivuos:${PASSWORD}@product.jlzub.mongodb.net/mcqApplication?retryWrites=true&w=majority`;

mongoose.connect(URL);
const db = mongoose.connection;
db.on("error", (error) => {
    console.log(error);
});
db.once("open", () => console.log("connected to database"));

app.use(function(req, res, next) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader(
        "Access-Control-Allow-Methods",
        "GET, POST, OPTIONS, PUT, PATCH, DELETE"
    );
    res.setHeader(
        "Access-Control-Allow-Headers",
        "X-Requested-With,content-type"
    );
    res.setHeader("Access-Control-Allow-Credentials", true);
    next();
});

app.use(express.json());

app.get("/", async(req, res) => {
    schema.find({}, (err, dat) => {
        if (err) {
            res.json({ error: err });
        } else {
            res.json({ data: dat });
        }
    });
    // a = new schema({
    //     question: "test",
    //     option_arr: [],
    //     answer: "answer_test",
    // });
    // await a.save();
    // res.json({ msg: "data added" });
});

app.listen(PORT);