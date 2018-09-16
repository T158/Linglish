import json

from django.core.management.base import BaseCommand

from ...models import Item


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help import_itemで表示されるメッセージ
    help = 'Create Item from json file'

    def remove_null(self, value, default):
        if value is None:
            return default
        return value

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):

        # ファイルのオープン
        with open('web.json', 'r') as file:

            # JSONの読み込み
            data = json.load(file)
            count = 0

            # 取得したデータを1件づつ取り出す
            for item_obj in data:

                if not item_obj['word']:
                    continue

                # Itemの保存処理
                item = Item()
                item.number = self.remove_null(item_obj['number'], '')
                item.word = self.remove_null(item_obj['word'], '')
                item.meaning = self.remove_null(item_obj['meaning'], '')
                item.example = self.remove_null(item_obj['example'], '')
                item.save()

                count += 1
                print('Create Item: {0}'.format(item.word))

            print('{} items have been created.'.format(count))