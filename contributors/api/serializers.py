from rest_framework.serializers import ModelSerializer
from contributors.models import Contributor
from rest_framework.fields import SerializerMethodField

class ContributorSerializer(ModelSerializer):

    contributor_type = SerializerMethodField()

    class Meta:
        model = Contributor
        fields = (
            'id', 'name', 'contributor_type', 'email', 'country'
        )

    def get_contributor_type(self,obj):
        return '%s %s %s' % (obj.author, obj.editor, obj.reviewer)
