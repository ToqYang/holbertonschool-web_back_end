// Clean set with strings coincidences

const cleanSet = (set, startString) => {
  const str = [];

  if (
    typeof set !== "object" ||
    startString instanceof String ||
    startString.length === 0
  ) {
    return "";
  }

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      str.push(item.slice(startString.length));
    }
  }

  return str.join("-");
};

export default cleanSet;
