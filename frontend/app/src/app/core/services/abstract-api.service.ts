export abstract class AbstractApiService {
  abstract postImage(base64Image: string): Promise<any>;
  abstract getImage(imageId: string): Promise<any>;
  abstract getItemDetails(itemId: string): Promise<any>;
  abstract getItem(): Promise<any>;
  abstract getMultimedia(multimediaTag: string): Promise<any>;
  abstract getHistory(): Promise<any>;
}
