from abc import ABC, abstractmethod


class BaseVideoModel(ABC):
    name: str = "base"
    
    @abstractmethod
    def generate_text_to_video(self, prompt: str, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def generate_image_to_video(self, image_path: str, prompt: str, **kwargs):
        raise NotImplementedError


class MockVideoModel(BaseVideoModel):
    name = "mock"
    
    def generate_text_to_video(self, prompt: str, **kwargs):
        return {
            "prompt": prompt,
            "status": "generated",
            "backend": self.name,
            "config": kwargs
        }
    
    def generate_image_to_video(self, image_path: str, prompt: str, **kwargs):
        return {
            "image_path": image_path,
            "prompt": prompt,
            "status": "generated",
            "backend": self.name,
            "config": kwargs
        }
