package  
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.filesystem.*;
	import class_314;

	public class Main extends Sprite
	{

		public function Main():void
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(e:Event = null):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			var file:File = new File("D:\\Programs\\Pyton273\\zombot_2014_1_Cheater\\sig\\bin\\url.txt");
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			this.serverUrl = stream.readUTFBytes(file.size);
			stream.close();
			//this.serverUrl = "http://java.shadowlands.ru/zombievk";
			file = new File("D:\\Programs\\Pyton273\\zombot_2014_1_Cheater\\sig\\bin\\keys.txt");
			stream = new FileStream();
			//this.serverUrl = "http://java.shadowlands.ru/zombievk";
			//var file:File = new File("C:\\Python27\\ZomBotSnow____maxim\\sig\\bin\\keys.txt");
			//var stream:FileStream = new FileStream();
			stream.open(file, FileMode.READ);
			var contents:Array = stream.readUTFBytes(file.size).split(" ");
			stream.close();
			this.authKey = contents[0];
			this.var_290 = new Number(contents[1]);
			this.sessionKey = contents[2];
			getSalt();

		}

		private var serverUrl:String;

		private var sessionKey:String;

		public var sigSaltFunc:Function;

		private var var_290:Number;

		private var authKey:String;

		  private function getSalt():void
         {
            var loadSaltComplete:Function = null;
            loadSaltComplete = function(param1:class_314):void
            {
               sigSaltFunc = param1.saltFunc;
               timeGetOk();
            };
            var postfix:String = sessionKey.substring(sessionKey.indexOf(":") + 1);
            new class_314(serverUrl,postfix,loadSaltComplete);
         };

		private function timeGetOk():void
		{
			var file:File = new File("D:\\Programs\\Pyton273\\zombot_2014_1_Cheater\\sig\\bin\\sig.txt");
			var stream:FileStream = new FileStream();
			stream.open(file, FileMode.WRITE);
			var output:Array = new Array();
			var id:Number;
			var sig:String;
			for (var i:Number = 0; i < 1000; i++) {
				id = var_290 + i;
				sig = this.sessionKey + id.toString() + this.authKey;
                sig = sig + this.sigSaltFunc(sig);
				output[i]= new String("\""+id.toString()+"\":\""+sig+"\"")
			}
			stream.writeUTFBytes("{"+output.join(",\n")+"}");
			stream.close();
			stage.nativeWindow.close();
		}


	}

}