module.exports = {
  apps: [
    {
      name: "balance-logger",
      script: "src/balancelog.py",
      interpreter: "./venv/bin/python",
      args: "--config walletconf.toml",
      watch: false
    }
  ]
};
