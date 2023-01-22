const mongoose = require("mongoose");

const schema = new mongoose.Schema({
    question: {
        type: String,
        required: true,
    },
    option_arr: {
        type: Array,
        required: true,
    },
    answer: {
        type: String,
        required: true,
    },
});

module.exports = {
    question: mongoose.model("data", schema),
};