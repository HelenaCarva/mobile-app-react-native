const { Parser } = require('recast');

const parseAST = (source) => {
  const result = {
    errors: [],
    ast: null,
  };

  try {
    const ast = Parser.parse(source);
    result.ast = ast;
  } catch (error) {
    result.errors.push(error);
  }

  return result;
};

module.exports = { parseAST };