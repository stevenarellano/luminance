import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BASEURL } from 'src/constants';

@Injectable({
  providedIn: 'root',
})
export class CurriculumService {
  curriculum: any[] | null = null;
  loading = false; // Add a loading variable

  constructor(private http: HttpClient) {}

  getCurriculum(topic: string) {
    const url = `${BASEURL}/upload?topic=${topic}`;
    this.loading = true; // Set loading to true before making the HTTP request
    this.http.get(url).subscribe((data: any) => {
      console.log(data);
    });
    return this.http.get(url).subscribe((data: any) => {
      this.loading = false; // Set loading to false when the request completes
      this.curriculum = data;
    });
  }
}
