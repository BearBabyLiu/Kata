package test.scala.com.liuhuang

import main.scala.com.liuhuang.{ArgsParser, CommandLineArgs, SchemaParser}
import org.scalatest.FeatureSpec

class ArgsParserSuite  extends FeatureSpec{

  feature("命令行参数解析") {
    scenario("当flag有值时能获取正确的值") {
      assert(CommandLineArgs("-b Ture -p 800 -d nihao").extractFlagVaule("-b") == "Ture")
      assert(CommandLineArgs("-b Ture -p 800 -d nihao").extractFlagVaule("-p") == "800")
      assert(CommandLineArgs("-b Ture -p 800 -d nihao").extractFlagVaule("-d") == "nihao")
    }

    scenario("当flag没有值时能获取正确的值") {
      assert(CommandLineArgs("-b  -p800 -d nihao").extractFlagVaule("-b") == "")
      assert(CommandLineArgs("-b Ture -p  -d nihao").extractFlagVaule("-p") == "")
      assert(CommandLineArgs("-b Ture -p 800 -d ").extractFlagVaule("-d") == "")
    }
  }

  feature("模板参数解析") {
    scenario("当输入-b:Boolean:false") {
      assert(SchemaParser("-b:Boolean:false").getType("-b") == "Boolean")
      assert(SchemaParser("-b:Boolean:false").getDefault("-b") == "false")
      assert(SchemaParser("-b:Boolean:false").getDefault("-c") == "")
    }

    scenario("当输入-p:Int:0") {
      assert(SchemaParser("-p:Int:0").getType("-p") == "Int")
      assert(SchemaParser("-p:Int:0").getDefault("-p") == "0")
      assert(SchemaParser("-p:Int:0").getDefault("-c") == "")
    }

    scenario("当输入-d:String:") {
      assert(SchemaParser("-d:String:").getType("-d") == "String")
      assert(SchemaParser("-d:String:").getDefault("-d") == "")
    }

    scenario("当输入-b:Boolean:false,-p:Int:0,-d:String:") {
      assert(SchemaParser("-b:Boolean:false,-p:Int:0,-d:String:").getType("-d") == "String")
      assert(SchemaParser("-b:Boolean:false,-p:Int:0,-d:String:").getType("-b") == "Boolean")
      assert(SchemaParser("-b:Boolean:false,-p:Int:0,-d:String:").getType("-p") == "Int")
      assert(SchemaParser("-b:Boolean:false,-p:Int:0,-d:String:").getDefault("-b") == "false")
      assert(SchemaParser("-b:Boolean:false,-p:Int:0,-d:String:").getDefault("-p") == "0")
      assert(SchemaParser("-b:Boolean:false,-p:Int:0,-d:String:").getDefault("-d") == "")
    }
  }

  feature("依据模板检查命令行参数") {
    scenario("根据模板能够获取正确的值") {
      assert(ArgsParser("-b True -p 800 -d nihao", "-b:Boolean:false,-p:Int:0,-d:String:").outFlagVaule("-b") == true)
      assert(ArgsParser("-b True -p 800 -d nihao", "-b:Boolean:false,-p:Int:0,-d:String:").outFlagVaule("-p") == 800)
      assert(ArgsParser("-b True -p 800 -d nihao", "-b:Boolean:false,-p:Int:0,-d:String:").outFlagVaule("-d") == "nihao")
      assert(ArgsParser("-b  -p 800 -d ", "-b:Boolean:false,-p:Int:0,-d:String:").outFlagVaule("-b") == false)
      assert(ArgsParser("-b  -p 800 -d ", "-b:Boolean:false,-p:Int:0,-d:String:").outFlagVaule("-p") == 800)
      assert(ArgsParser("-b  -p 800 -d ", "-b:Boolean:false,-p:Int:0,-d:String:").outFlagVaule("-d") == "")
    }

  }

}
