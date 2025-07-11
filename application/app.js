const express = require("express");
const app = express();
const defectRouter = require("./routes/defect");
const defectController = require("./controllers/defectController");
const errorHandler = require("./middleware/errorHandler");
app.use(express.json());
app.use("/api/defects", defectRouter);
app.post("/api/defects/logDefect", defectController.logDefect);
app.use(errorHandler);
const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});