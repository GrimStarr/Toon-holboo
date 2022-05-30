const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

app.use(express.json());

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("start");
});
app.get("/lab3", (req, res) => {
  const yaml = require("js-yaml");
  const fs = require("fs");

  // Get document, or throw exception on error
  try {
    const doc = yaml.load(fs.readFileSync("./lab3.grc", "utf8"));
    console.log(doc.options.parameters.title);
    res.render("lab3", {
      data: {
        title: doc.options.parameters.title,
        output_language: doc.options.parameters.output_language,
        generate_options: doc.options.parameters.generate_options,
        block_freq: doc.blocks[0].name,
        block_freq_label: doc.blocks[0].parameters.label,
        block_freq_start: doc.blocks[0].parameters.start,
        block_freq_end: doc.blocks[0].parameters.end,
        block_freq_value: doc.blocks[0].parameters.value,
        block_freq_throt: doc.blocks[0].parameters.throttle,
        noise_amp: doc.blocks[1].name,
        noise_amp_label: doc.blocks[1].parameters.label,
        noise_amp_start: doc.blocks[1].parameters.start,
        noise_amp_end: doc.blocks[1].parameters.end,
        noise_amp_value: doc.blocks[1].parameters.value,
        noise_amp_throt: doc.blocks[1].parameters.throttle,
        signal_amp: doc.blocks[3].name,
        signal_amp_label: doc.blocks[3].parameters.label,
        signal_amp_start: doc.blocks[3].parameters.start,
        signal_amp_end: doc.blocks[3].parameters.end,
        signal_amp_value: doc.blocks[3].parameters.value,
        signal_amp_throt: doc.blocks[3].parameters.throttle,
        variable: doc.blocks[2].name,
        variable_val: doc.blocks[2].parameters.value,
        noise_source_seed: doc.blocks[4].parameters.seed,
        signal_source_offset: doc.blocks[5].parameters.offset,
        signal_source_phase: doc.blocks[5].parameters.phase,
        bokeh_gui_freq_fft: doc.blocks[8].parameters.fftsize,
        bokeh_gui_freq_center: doc.blocks[8].parameters.fc,
        bokeh_gui_time_points: doc.blocks[9].parameters.size,
      },
    });
  } catch (e) {
    console.log(e);
  }
});

app.listen(port, () => console.log(`listening on port ${port}!`));

process.on("unhandledRejection", (err, promise) => {
  console.log(`Алдаа гарлаа: ${err.message}`);
  server.close(() => {
    process.exit(1);
  });
});
