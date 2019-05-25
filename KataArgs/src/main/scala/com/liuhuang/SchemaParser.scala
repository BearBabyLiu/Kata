package main.scala.com.liuhuang


case class SchemaParser(schemaArgs: String){

  val schemaData: Array[ArgType] = schemaArgs.split(",").map(x => {
    val schema  = x.split(":")
    schema(SchemaEnum.VALUE_TYPE) match {
      case "Boolean" => new BoolType(schema(SchemaEnum.FLAG), schema(SchemaEnum.DEFAULT_VALUE))
      case "Int" => new IntType(schema(SchemaEnum.FLAG), schema(SchemaEnum.DEFAULT_VALUE))
      case "String" => new StringType(schema(SchemaEnum.FLAG), "")
      case _ => new NullType
    }
  })

  def getType(flag: String): String = {
    filterArgType(flag).getType
  }

  def getDefault(flag: String): String = {
    filterArgType(flag).getDefault
  }

  def filterArgType(flag: String): ArgType = {
    val schema = schemaData.filter(x =>x.getFlag == flag)
    if(schema.nonEmpty) return schema.head
    new NullType()
  }

}
