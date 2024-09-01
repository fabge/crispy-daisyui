/** @type {import('tailwindcss').Config} */

const Path = require("path");
const { execSync } = require('child_process');
// const pySitePackages = execSync('python -c "import site; print(site.getsitepackages()[0])"').toString().trim();
const pySitePackages = '../'

let pyPackagesPaths = [
    Path.join(pySitePackages, "crispy_daisyui/**/*.html"),
    Path.join(pySitePackages, "crispy_daisyui/**/*.py"),
    Path.join(pySitePackages, "crispy_daisyui/**/*.js"),
];

console.log(pyPackagesPaths);
module.exports = {
  content: [
    'templates/**/*.html',
    'app1/**/*.py',
    ...pyPackagesPaths
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui")
  ]
}
