module.exports = {
  root: true,
  env: {
    browser: true,
    es6: true,
    jest: true
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module'
  },
  settings: {
    react: {
      version: 'detect'
    }
  },
  extends: ['plugin:react/recommended', 'plugin:react-native/all'],
  plugins: ['react', 'react-native'],
  rules: {
    'no-console': 'warn',
    'no-unused-vars': 'warn',
    'react-native/split-platform-components': 'warn'
  },
  parser: 'babel-eslint'
};
