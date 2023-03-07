from rest_framework import serializers
from snippets.models import Snippet ,LANGUAGEE_CHOICES,STYLE_CHOICES
# from tutorial.snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank=True,max_length=100)
    code = serializers.CharField(style = {'base_template':'text_area.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGEE_CHOICES , defaults='python')
    style = serializers.ChoiceField(style=STYLE_CHOICES , default='friently')


    def create(self , validated_data):
        """create and return a new instance of snippet given the validated data..."""
        return Snippet.object.create(**validated_data)

    def update(self , instance ,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code',instance.code)
        instance.linenos = validated_data.get('linenos',instance.linenos)
        instance.language = validated_data.get('language',instance.language)
        instance.style = validated_data.get('style',instance.style)
        instance.save()
        return instance