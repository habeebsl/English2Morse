from rest_framework import serializers


class ApiSerializerClass(serializers.Serializer):

    translate = serializers.CharField(max_length=15)
    text = serializers.CharField(max_length=1000)

    def validate_translate(self, data):
        translate = data
        if translate == "morse" or translate == "english":
            return data
        raise serializers.ValidationError(f" \'translate\' must be english or morse")


