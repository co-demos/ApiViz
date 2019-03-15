

// >>> LEGACY FILTERS / CREATION - LOW LEVEL FUNCTION
export function makeEmptySelectedFilters(filterDescriptions){
  console.log("::: makeEmptySelectedFilters / filterDescriptions : ", filterDescriptions)
  const selectedFilters = new Map()
  for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
  }
  return selectedFilters;
}

export function textFromLocale(textsList, locale, field){
  // console.log("::: textFromLocale / textsList : ", textsList)
  // console.log("::: textFromLocale / locale : ", locale)
  // console.log("::: textFromLocale / field : ", field)
  let textObject = textsList.find(t => t.locale == locale )
  let textOut = textObject[field]
  // console.log("::: textFromLocale / textOut : ", textOut)
  return textOut
}