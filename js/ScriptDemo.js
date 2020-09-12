let {PythonShell} = require('python-shell')
 
PythonShell.run('scrape.py', null, function (err) {
  if (err) throw err;
});
